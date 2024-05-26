import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import NavBar from '../components/navBar';
import ControlCarousel from '../components/carousel';
import SideMenu from '../components/sideMenu';
import ProgressControl from '../components/progressControl';

function Home () {
  const [openMenu, setOpenMenu] = useState(false);
  const toggleOpenMenu = () => {
    if (openMenu) {
      setOpenMenu(false);
    } else {
      setOpenMenu(true);
    }
  }

    return (
        <>
        <NavBar/>
        <Button onClick={toggleOpenMenu}>See the full list</Button>
        <SideMenu openMenu={openMenu} setOpenMenu={setOpenMenu} />
        <ProgressControl />
        <ControlCarousel />
        </>
    )
}

export default Home;