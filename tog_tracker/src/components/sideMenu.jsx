import Button from 'react-bootstrap/Button';
import Offcanvas from 'react-bootstrap/Offcanvas';

function SideMenu({openMenu, setOpenMenu}) {
  const toggleOpenMenu = () => {
    if (openMenu) {
      setOpenMenu(false);
    } else {
      setOpenMenu(true);
    }
  }

  return (
    <>

    </>
  );
}

export default SideMenu;