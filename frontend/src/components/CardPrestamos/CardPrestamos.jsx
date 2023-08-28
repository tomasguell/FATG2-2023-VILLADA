import React from 'react';

import './CardPrestamos.css'
import Stack from 'react-bootstrap/Stack';
import Table from 'react-bootstrap/Table';
import fotoPrueba2 from '../../assets/fotoPrueba2.jpg';
import PersonRoundedIcon from '@mui/icons-material/PersonRounded';
import {
  MDBCard,
  MDBCardBody,
  MDBCardHeader,
  MDBCardTitle,
  MDBCardText,
  MDBBtn
} from 'mdb-react-ui-kit';

<head>
  <link rel="preconnect" href="https://fonts.googleapis.com"></link>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin></link>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet"> </link>
</head>

export default function CardPrestamos() {
  return (
    <MDBCard border='none' style={{ fontFamily:'Roboto, sans-serif', fontSize:'0.938rem', boxShadow:'0 2px 4px rgba(0, 0, 0, 0.05)'}}>
      <MDBCardHeader className='card-header'>Mis Prestamos</MDBCardHeader>
      
        <Table className='card-table'>
          <tbody>
            <tr>
              <td>10 Enero, 2023</td>
            </tr>
          </tbody>
        </Table>
        <Stack direction='horizontal' gap={4}>
          <div className='p-2'>
            <img src={fotoPrueba2} alt="Paisaje" style={{width:'10rem'}}/>
          </div>
          <Stack>
            <div style={{marginTop:'0.2rem'}}>
              <p style={{fontSize:'0.938rem', color:'#45BE7F', margin:'0'}}>Entregado</p>
              <p style={{fontSize:'0.938rem'}}>6 productos</p>
            </div>
          </Stack>
          <Stack>
            <div style={{marginTop:'0.2rem'}}>
              <p style={{fontSize:'0.938rem', margin:'0'}}>Juan Frattin</p>
              <p style={{fontSize:'0.938rem', margin:'0'}}>6c Programacion</p>
            </div>
          </Stack>
          <Stack>
            <div style={{marginTop:'0.2rem'}}>
              <p style={{fontSize:'0.938rem', margin:'0'}}>Nacho no sabe que poner</p>
              <p style={{fontSize:'0.938rem', margin:'0'}}>Asi que hasta que no lo complete</p>
              <p style={{fontSize:'0.938rem'}}>Yo tampoco</p>
            </div>
          </Stack>
          <Stack>
          </Stack>
        </Stack>
      
    </MDBCard>
  );
}