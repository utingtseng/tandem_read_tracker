import { useState, useEffect } from 'react';
import Offcanvas from 'react-bootstrap/Offcanvas';
const API_URL = 'http://127.0.0.1:5000';

function SideMenu({openMenu, setOpenMenu}) {

  const handleClose = () => setOpenMenu(false);
  const [fullList, setFullList] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/tandem/full-list`)
      .then((res) => {
        console.log('Response status:', res.status);
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log('Response data:', data);
        setFullList(data);
      })
      .catch((error) => {
        console.error('Fetch error:', error);
      });
  }, []);

  return (
    <>
    <Offcanvas show={openMenu} onHide={handleClose} placement="end">
      <Offcanvas.Header closeButton>
      <Offcanvas.Title>Full tandem read list</Offcanvas.Title>
      </Offcanvas.Header>
      <Offcanvas.Body>
      {fullList.map((section) => {
        return(
          <li>
            {section.title}- {section.chapters} {section.read? "✅": "📖"}
          </li>
        )
      })}
      </Offcanvas.Body>
    </Offcanvas>
    </>
  );
}

export default SideMenu;