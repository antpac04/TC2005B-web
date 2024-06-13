import Plot from "react-plotly.js";
import React from 'react';


function GenderScores({ scores, nivel }) {
  const traces = {};


  scores.forEach((score) => {
    if (score.nivel != nivel) {
      return;
    }


    const { genero, valor } = score;
    if (!traces[genero]) {
        traces[genero] = {
            x: [],
            y: [],
            type: 'box',
            name: genero
        };
    }
    traces[genero].y.push(valor);
  });


  const data = Object.values(traces);


  return (
    <Plot
      data={data}
      layout={{
        title: `Distribución de Puntuaciones de nivel ${nivel} por Género`,
        yaxis: {
          title: 'Puntuación'
        },
        boxmode: 'group',
        autosize: true,
      }}
      useResizeHandler={true}
      style={{
        width: "100%",
        height: "100%",
      }}
    />
  );
}


export default GenderScores;
