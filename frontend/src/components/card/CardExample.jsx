import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import './CardExample.css';
export default function CardExample(props) {
  const {id, name, title, image, text}=props;
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={image} />
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <Card.Text>
          {text}
        </Card.Text>
        <Button variant="primary">Agregar Al carrito</Button>
      </Card.Body>
    </Card>
  );
}

 