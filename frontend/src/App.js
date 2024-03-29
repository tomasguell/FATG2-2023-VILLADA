import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import useAxios from './utils/useAxios';
import HomePage from './pages/Home/HomePage';
import DetalleCuenta from './pages/DetalleCuenta/DetalleCuenta';
import DetalleProducto from './pages/DetalleProducto/DetalleProducto';
import Layout from './BaseLayout/Layout';
import Ecommerce from './pages/Ecommerce/Ecommerce.jsx';
import Carrito from './pages/Carrito/Carrito.jsx';
import './assets/styles/App.css';
import Home from './pages/LoginNuevo/home';
import MainWrapper from './layouts/MainWrapper';
import Login from './pages/LoginNuevo/login';
import PrivateRoute from './layouts/PrivateRoute';
import Logout from './pages/LoginNuevo/logout';
import Register from './pages/LoginNuevo/register';
import Private from './pages/LoginNuevo/private';
import Prestamos from './pages/Prestamos/Prestamos';
import { useAuthStore } from './store/auth';
import Presupuestos from './pages/Presupuestos/Presupuestos';
import DetallePresupuesto from './pages/DetallePresupuesto/DetallePresupuesto';
import { Link } from 'react-router-dom';
import Informes from './pages/Informes/Informes';
import DetallePrestamo from './pages/DetallePrestamo/DetallePrestamo';

function App() {
  const api = useAxios();
  const [user] = useAuthStore((state) => [
    state.user,
  ]);

  const user_id = user().user_id;
  const [userData, setUserData] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [isUserProfessor, setIsUserProfessor] = useState(false);

  const handleSearch = (query) => {
    setSearchQuery(query);
    console.log(query);
  };

  const isProfessor = (groups) => {
    if (!groups || groups.length === 0) {
      // Si no tiene grupos, no es profesor
      return false;
    }
    
    // Verifica si al menos uno de los grupos es "Profesor"
    return !groups.includes("Alumno");
  };

  useEffect(() => {
    if (user_id) {
      try {
        api.get(`users/${user_id}/`)
          .then((response) => {
            setUserData(response.data);
            setIsUserProfessor(isProfessor(response.data.groups));
          })
          .catch((error) => {
            console.error(error);
          });
      } catch (error) {
        console.error(error);
      }
    }
  }, [user_id]);

  return (
    <Router>
      <MainWrapper>
        <div className="container">
          <div className="app">
            <Routes>
              <Route path="/private" element={<PrivateRoute><Private /></PrivateRoute>} />
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<Register />} />
              <Route path="/logout" element={<Logout />} />
              <Route path="/*" element={<LayoutWrapper onSearch={handleSearch} searchQuery={searchQuery} isProfessor={isUserProfessor}/>} />
            </Routes>
          </div>
        </div>
      </MainWrapper>
    </Router>
  );
}

function LayoutWrapper({ onSearch, searchQuery, isProfessor }) {
  return (
    <Layout isProfessor={isProfessor}>
      <Routes>
        {isProfessor ? (
          <Route path="/informe" element={<PrivateRoute><Informes isProfessor={isProfessor} /></PrivateRoute>} />
        ) : null}
        <Route path="/" element={<PrivateRoute><HomePage /></PrivateRoute>} />
        <Route path="/tienda" element={<PrivateRoute><Ecommerce allItems={true} /></PrivateRoute>} />
        <Route path="/tienda/:name" element={<PrivateRoute><Ecommerce allItems={false} /></PrivateRoute>} />                          
        <Route path="/carrito" element={<PrivateRoute><Carrito /></PrivateRoute>} />
        <Route path="/detalleProducto/:id" element={<PrivateRoute><DetalleProducto /></PrivateRoute>} />
        <Route path="/detalleCuenta" element={<PrivateRoute><DetalleCuenta /></PrivateRoute>} />
        {isProfessor ? (
          <Route path="/presupuesto" element={<PrivateRoute><Presupuestos /></PrivateRoute>} />
        ) : null}
        {isProfessor ? (
          <Route path="/presupuesto/:id" element={<PrivateRoute><DetallePresupuesto /></PrivateRoute>} />
        ) : null}
        <Route path="/detallePrestamo/:dateId/" element={<PrivateRoute><DetallePrestamo  /></PrivateRoute>} />
        <Route path="/Prestamos" element={<PrivateRoute><Prestamos /></PrivateRoute>} />
      </Routes>
    </Layout>
  );
}

export default App;
