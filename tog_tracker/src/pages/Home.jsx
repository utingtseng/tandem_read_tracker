import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Offcanvas from 'react-bootstrap/Offcanvas';
import NavBar from '../components/navBar';
import DisplayCurrent from '../components/displayCurrent';

function Home () {
    const [openMenu, setOpenMenu] = useState(false);
    const toggleOpenMenu = () => {
        if (openMenu) {
          setOpenMenu(false);
        } else {
          setOpenMenu(true);
        }
      }
    const handleClose = () => setOpenMenu(false);
    const handleShow = () => setOpenMenu(true);
    return (
        <>
        <NavBar/>
        <Button onClick={toggleOpenMenu}>Open drawer</Button>
        <Offcanvas show={openMenu} onHide={handleClose}>
            <Offcanvas.Header closeButton>
            <Offcanvas.Title>Offcanvas</Offcanvas.Title>
            </Offcanvas.Header>
            <Offcanvas.Body>
            Some text as placeholder. In real life you can have the elements you
            have chosen. Like, text, images, lists, etc.
            </Offcanvas.Body>
        </Offcanvas>
        <DisplayCurrent />
        </>
    )
}

export default Home;