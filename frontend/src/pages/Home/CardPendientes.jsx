import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import useAxios from '../../utils/useAxios';
import Table from 'react-bootstrap/Table';
import {
  MDBBadge,
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardText,
  MDBCardHeader,
  MDBCardFooter,
  MDBBtn,
  MDBListGroup,
  MDBListGroupItem,
  MDBTable,
  MDBTableHead,
  MDBTableBody,
} from 'mdb-react-ui-kit';
import { useAuthStore } from '../../store/auth';
 

// ... (imports and other code)

const CardPendientes = () => {
  const api = useAxios();
  const [element, setElement] = useState([]);
  const [isLoggedIn, user] = useAuthStore((state) => [
    state.isLoggedIn,
    state.user,
  ]);

  useEffect(() => {
    getElement();
  }, []);

  const getElement = async () => {
    try {
      const response = await api.get(`/pendientes/${userData.user_id}`);
      let data = await response.data;
      setElement(data);
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  };

  const userData = user();

  // Función para formatear una cadena de fecha y hora en solo fecha
  const formatDate = (datetimeString) => {
    const dateObject = new Date(datetimeString);
    const year = dateObject.getFullYear();
    const month = (dateObject.getMonth() + 1).toString().padStart(2, '0');
    const day = dateObject.getDate().toString().padStart(2, '0');

    return `${year}-${month}-${day}`;
  };

  return (
    <MDBCard alignment='left' style={{ backgroundColor: 'white', border: 'none', width: '33%', minHeight: '40vh', maxHeight: '50vh', minWidth: '50vh' }}>       
     <MDBCardHeader style={{ color: 'white' }}>Pendientes</MDBCardHeader>
      <Table hover style={{ marginBottom: '0', height: '100%' }}>
                <thead>
          <tr>
            <th scope='col'>Fecha</th>
            <th scope='col'>Producto</th>
            <th scope='col'>Cantidad</th>
          </tr>
        </thead>
        <tbody>
        {element.slice(-4).map((item, index) => (
            <tr key={index}>
              <td>{formatDate(item.dateOut)}</td> {/* Display formatted date */}
              <td>{item.box.name.length > 10? item.box.name.slice(0, 10) + '...' : item.box.name}</td>      
             <td>{item.quantity}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </MDBCard>
  );
};

export default CardPendientes;