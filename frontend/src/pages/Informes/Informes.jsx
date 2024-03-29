import React, { useState, useEffect } from 'react';
import './Informes.css';
import MostRequestedElements from './MostRequestedElements';
import TasaVencidos from './TasaVencidos';
import TasaAprobacion from './TasaAprobacion';
import DiaDemandado from './DiaDemandado';
import TiempoPorPrestamo from './TiempoPorPrestamo';
import HorizontalBarChart from './HorizontalBarChart';
import VerticalBarChart from './VerticalBarChart';

function Informes({ isProfessor }) {
  const [deudorData, setDeudorData] = useState([]);
  const [boxData, setBoxData] = useState([]);
  console.log(isProfessor)
  useEffect(() => {
    fetch('/api/estadisticas/mayordeudor/')
      .then(response => response.json())
      .then(data => setDeudorData(data))
      .catch(error => console.error('Error fetching deudor data:', error));

    fetch('/api/estadisticas/box_mas_logs_rotos/')
      .then(response => response.json())
      .then(data => setBoxData(data))
      .catch(error => console.error('Error fetching box data:', error));
  }, []);

  return (
    <div className="container pagecontainer" style={{marginLeft:'125px'}}>
      <div className="row">
        {/* Fila 1 */}
        <div className="col-md-4">
          <TasaVencidos endpoint="estadisticas/vencidos/" />
        </div>
        <div className="col-md-4">
          <TasaAprobacion endpoint="estadisticas/aprobado/" />
        </div>
        
        <div className="col-md-4">
  <div className="d-flex flex-column align-items-start" style={{ marginLeft: '11px' }}>
    <TiempoPorPrestamo />
    <DiaDemandado subtitle="Día que más se pide" />
  </div>
</div>

      </div>

      <div className="row" style={{ marginTop: '30px' }}>
        {/* Fila 2 */}
        <div className="col-md-8">
          <h4>Top deudores</h4>
          <HorizontalBarChart data={deudorData} />
        </div>
        <div className="col-md-4">
          <MostRequestedElements endpoint="estadisticas/maspedido/" />
        </div>
      </div>

      <div className="col-md-8 d-flex flex-column" style={{ width: '900px', height: '300px' }}>
  <h4>Box que mas se rompen</h4>
  <VerticalBarChart data={boxData} />
</div>
      
    </div>
    
  );
}

export default Informes;
