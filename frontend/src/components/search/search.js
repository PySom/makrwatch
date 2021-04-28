import './search.css';
import { useInput } from '../../hooks/use_input';
import AppButton from '../app_button/app_button';
import AppIcon from '../app_icon/app_icon';
import { useHistory } from 'react-router';

function Search() {
    const searchProps = useInput('', 'email');
    const history = useHistory();
    const onSearch = () => {
        if (searchProps.value?.length >= 3) {
            history.push(`/search?term=${searchProps.value}`)
        }
    }
    return (
        <div className='d-flex search full-width'>
            <input {...searchProps} className='flex-one z-index2' placeholder='Search topics on the videos you want to find' />
            <AppButton onClick={onSearch} />
        </div>
    );
}

export default function SearchArea() {
    return (
        <div className='search-area'>
            <div className='d-flex flex-vertical align-center'>
                <AppIcon />
                <Search />
            </div>
        </div>
    );
}