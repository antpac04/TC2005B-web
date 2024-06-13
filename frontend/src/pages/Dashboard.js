import { useEffect, useState } from "react";
import TimeSeries from "../components/TimeSeries";
import BarChart from "../components/BarChart";
import Navbar from "../components/Navbar";
import GenderScores from "../components/GenderScores";
import BarPuntaje from "../components/Bar_Puntaje";

function Dashboard() {

  const [isLoading, setIsLoading] = useState(true);
  const [scores, setScores] = useState();
  const [nivel, setNivel] = useState(1);

  async function getScores() {
    setIsLoading(true);
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/puntuaciones`);
    const data = await response.json();
    setScores(data);
    setIsLoading(false);
  }

  useEffect(() => {
    getScores();
  }, []);

  if (isLoading) {
    return <div className="loading">Cargando . . .</div>
  }

  return (
    <>
      <Navbar/>
      <main className="dashboard-content">
        <h1>Gráficas</h1>
        <p className="description">
          Consulta información sobre los puntajes de los estudiantes bajo diferentes 
          categorías. Selecciona el nivel deseado del menú, o bien selecciona el estudiante deseado, para filtrar. 
          Utiliza los controles para ajustar el zoom en las gráficas.
        </p>
        <section className="graph-container">
          <article className="graph-card">
            <h2>Puntuaciones vs Tiempo</h2> 
            <label htmlFor="nivel-select" className="nivel-label">Nivel:</label>
            <select id="nivel-select" value={nivel} onChange={(event) => { setNivel(parseInt(event.target.value)); }} className="nivel-select">
              <option value="1">Nivel 1</option>
              <option value="2">Nivel 2</option>
              <option value="3">Nivel 3</option>
            </select>
            <TimeSeries scores={scores} nivel={nivel} />
          </article>
          
          <article className="graph-card">
            <h2>Tiempo por Nivel</h2>
            <label htmlFor="nivel-select-bar" className="nivel-label">Nivel:</label>
            <select id="nivel-select-bar" value={nivel} onChange={(event) => { setNivel(parseInt(event.target.value)); }} className="nivel-select">
              <option value="1">Nivel 1</option>
              <option value="2">Nivel 2</option>
              <option value="3">Nivel 3</option>
            </select>
            <BarChart scores={scores} nivel={nivel} />
          </article>

          <article className="graph-card">
            <h2>Distribución de Puntuaciones por Género</h2>
            <label htmlFor="nivel-select-gender" className="nivel-label">Nivel:</label>
            <select
              id="nivel-select-gender"
              value={nivel}
              onChange={(event) => {
                setNivel(Number(event.target.value));
              }}
              className="nivel-select"
            >
              <option value="1">Nivel 1</option>
              <option value="2">Nivel 2</option>
              <option value="3">Nivel 3</option>
            </select>
            <GenderScores scores={scores} nivel={nivel} />
          </article>


          <article className="graph-card">
            <h2>Puntaje general de los alumnos</h2>
            <BarPuntaje scores={scores}></BarPuntaje>
          </article>
        </section>
      </main>
    </>
  );

}

export default Dashboard;
