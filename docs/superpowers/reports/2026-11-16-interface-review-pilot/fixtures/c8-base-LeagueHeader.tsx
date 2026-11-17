import { ShareIcon, MenuIcon } from './icons';

type Props = {
  name: string;
  avatarUrl: string;
  onShare: () => void;
  onOpenMenu: () => void;
};

export function LeagueHeader({ name, avatarUrl, onShare, onOpenMenu }: Props) {
  return (
    <header className="league-header">
      <img src={avatarUrl} className="league-avatar" />
      <h1 className="league-title">{name}</h1>
      <button type="button" className="icon-button" aria-label="Compartir liga" onClick={onShare}>
        <ShareIcon aria-hidden="true" />
      </button>
      <button type="button" className="icon-button" aria-label="Abrir menú" onClick={onOpenMenu}>
        <MenuIcon aria-hidden="true" />
      </button>
    </header>
  );
}
