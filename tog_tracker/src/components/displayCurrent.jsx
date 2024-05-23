import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import eos from '../assets/empireofstorm.jpg';

function DisplayCurrent () {
    return (
        <Container>

        <Row>
        <Card className="text-white">
            <Card.Img src={eos} alt="Card image" />
            <Card.ImgOverlay>
                <Card.Title>Card title</Card.Title>
                <Card.Text>
                This is a wider card with supporting text below as a natural lead-in
                to additional content. This content is a little bit longer.
                </Card.Text>
                <Card.Text>Last updated 3 mins ago</Card.Text>
            </Card.ImgOverlay>
        </Card>
          <Col></Col>
        </Row>
      </Container>
    )
}

export default DisplayCurrent;