import { useEffect, useState } from 'react';
import { useLocation } from 'react-router';
import api from '../../api/api';
import AppButton from '../app_button/app_button';
import Loader from '../loader/loader';
import './search_result.css';

export default function SearchResults() {
    const location = useLocation();
    console.log(location.search)
    const [result, setResult] = useState();
    const [busy, setBusy] = useState(false);
    const [pageToken, setPageToken] = useState();

    useEffect(() => {
        getSearch('')
    }, [])

    const getSearchTerm = () => {
        const term = location.search
        if (term) {
            const splitQuery = term.split('&');
            const getQueryWithTerm = splitQuery.find(query => query?.toLocaleLowerCase().includes('term'));
            if (getQueryWithTerm) {
                const queryTerm = getQueryWithTerm.split('=');
                if (queryTerm.length === 2) {
                    const searchTerm = queryTerm[1];
                    return searchTerm;
                }

            }
        }
    }

    const getSearch = (url) => {
        const searchTerm = getSearchTerm()
        if (searchTerm) {
            if (searchTerm) {
                setBusy(true);
                api.get(`youtube/term/${searchTerm}` + url)
                    .then((data) => {
                        console.log({ data })
                        const newData = result ?
                            { ...result, nextPageToken: data.nextPageToken, items: [...result.items, ...data.items] }
                            : data
                        setResult(newData)
                        console.log(newData.nextPageToken)
                        setPageToken(newData.nextPageToken);
                        setBusy(false);
                    })
                    .catch(err => {
                        setBusy(false);
                        console.log(err)
                    })
            }


        }

    };

    const seeMoreVideos = () => {
        getSearch(`/pageToken/${pageToken}`);

    };
    return (
        <div>
            {busy && <Loader />}
            {getSearchTerm() && <p className='search-term'>Search result for "{getSearchTerm()}"</p>}
            {result && result.items.map((item, index) => <SearchResult key={item?.id?.videoId + '-' + index} snippet={item?.snippet} statistics={item?.statistics} videoId={item?.id?.videoId} />)}
            <div className='d-flex j-center'>
                <AppButton name='See more videos' onClick={seeMoreVideos} className='no-border-radius' />
            </div>
        </div>
    );
}


function SearchResult({ snippet, statistics, videoId }) {
    return (
        <div className='result-area'>
            <div className='d-flex-mobile-block'>
                <a target='_blank' rel="noreferrer" href={`https://youtube.com/watch?v=${videoId}`}>
                    <div className='youtube-image' style={{ backgroundImage: `url('${snippet?.thumbnails?.medium?.url}')` }}></div>
                </a>
                <div className='d-flex flex-vertical j-space-between'>
                    <div>
                        <p className='title'>{snippet?.title}</p>
                        <a target='_blank' rel="noreferrer" href={`https://youtube.com/channel/${snippet?.channelId}`} className='owner'>{snippet?.channelTitle}</a>
                        <p className='d-flex views-paragraph'><span className='views-figure'>{thousandSeparator(statistics?.viewCount)}</span> <span className='views'>Views</span></p>
                    </div>
                    <a target='_blank' rel="noreferrer" href={`https://youtube.com/watch?v=${videoId}`} className='description'>{snippet?.description || snippet?.title}</a>
                    <p className='duration'>{snippet?.publishedAt}</p>
                </div>
            </div>
            <hr />
        </div>
    );
}

function thousandSeparator(val) {
    const valAsNumber = Number(val);
    if (!isNaN(valAsNumber)) {
        return valAsNumber.toLocaleString();
    }
    else {
        return val;
    }
}