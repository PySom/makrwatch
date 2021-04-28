import './app_icon.css';
import appIcon from '../../assets/images/logo.png';

export default function AppIcon({ className }) {
	return (
		<img src={appIcon} className={(className || '') + ' app-icon'} alt='Makrwatch identity' />
	);
}