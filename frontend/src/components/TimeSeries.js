import Plot from "react-plotly.js";
import React from 'react'

function TimeSeries({ scores, nivel }) {
  const traces = {};
  scores.forEach((score) => {
    if (score.nivel !== nivel) {
      return;
    }
  
    const { id_estudiante, fecha, valor } = score;
    if (!traces[id_estudiante]) {
        traces[id_estudiante] = {
            x: [],
            y: [],
            type: 'scatter',
            mode: 'lines+markers',
            name: `Estudiante ${id_estudiante}`
        };
    }
    traces[id_estudiante].x.push(new Date(fecha));
    traces[id_estudiante].y.push(valor);
  });
  const data = Object.values(traces);


  return (
    <>
    <Plot
            data={data}
            layout={{
                title: `Puntuaciones de nivel ${nivel} a través del tiempo`,
                xaxis: {
                    title: 'Fecha',
                    type: 'date'
                },
                yaxis: {
                    title: 'Puntuación'
                },
                cornerRadius: "200px",
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

export default TimeSeries