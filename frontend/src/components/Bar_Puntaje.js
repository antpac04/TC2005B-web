import Plot from "react-plotly.js";
import React from 'react';

function BarPuntaje({ scores }) {
    const times = {};
  
    scores.forEach((score) => {
      const { id_estudiante, valor, nivel } = score;
      if (!times[id_estudiante]) {
        times[id_estudiante] = {
          x: [],
          y: [],
          type: 'bar',
          name: `Estudiante ${id_estudiante}`
        };
      }
      times[id_estudiante].x.push(`Estudiante ${id_estudiante}`);
      times[id_estudiante].y.push(valor);
    });
  
    const data = Object.values(times);
  
    return (
      <>
        <Plot
          data={data}
          layout={{
            title: `Puntaje general obtenido por todos los estudiantes`,
            xaxis: {
              title: 'Estudiantes',
              type: 'category'
            },
            yaxis: {
              title: 'Puntaje',
            },
            autosize: true,
            showlegend: true,
          }}
          useResizeHandler={true}
          style={{
            width: "100%",
            height: "100%",
          }}
        />
      </>
    );
  }
  
  export default BarPuntaje;
  

// function BarPuntajes({scores,estudiante}){
//     const bars = [];
//     const alumn = [];

//     scores.forEach((score) => {

//     })
// }