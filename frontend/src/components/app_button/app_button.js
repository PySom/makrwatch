import './app_button.css';
import search from '../../assets/images/search.png';

export default function AppButton({ className, onClick, type, name }) {
    return (
        <button className={`app-button ${className || ''}`} onClick={onClick} type={type || 'button'}>
            {name || <img src={search} alt='Search button' />}
        </button>
    );
}

