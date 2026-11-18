import { SearchIcon, BellIcon } from './icons';

type Props = { onSearch: () => void; onNotifications: () => void; unread: number };

export function Toolbar({ onSearch, onNotifications, unread }: Props) {
  return (
    <nav className="toolbar" aria-label="Acciones">
      <button type="button" className="icon-button" aria-label="Buscar" onClick={onSearch}>
        <SearchIcon aria-hidden="true" />
      </button>
      <button type="button" className="icon-button" aria-label={`Notificaciones, ${unread} sin leer`} onClick={onNotifications}>
        <BellIcon aria-hidden="true" />
      </button>
    </nav>
  );
}
