import Plot from "react-plotly.js";
import React from 'react';

function BarChart({ scores, nivel }) {
  const times = {};

  scores.forEach((score) => {
    if (score.nivel !== nivel) {
      return;
    }

    const { id_estudiante, valor} = score;
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
          title: `Tiempo emitido por los estudiantes en el nivel ${nivel}`,
          xaxis: {
            title: 'Estudiantes',
            type: 'category'
          },
          yaxis: {
            title: 'Tiempo (minutos)',
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

export default BarChart;
