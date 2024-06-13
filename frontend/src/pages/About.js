import Navbar from "../components/Navbar";

function About() {
    return (
      <>
        <Navbar/>
        <main className="dashboard-content">
          <h1>Acerca De</h1>
          <p className="description">
            Este portal permite conocer los puntajes de los alumnos bajo diferentes filtros. Consulta las gráficas en la sección correspondiente. Consulta la licencia en esta sección.
          </p>
          <p className="license">
            Licencia: Space Adventures © 2024 by Othón Berlanga Calderón, Wilfrido Tovar Andrade, Carlos Alberto Páez de la Cruz, José Antonio Pacheco Chargoy is licensed under Creative Commons Attribution 4.0 International. 
            To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
          </p>
        </main>
      </>
    );
  
  }
  
  export default About;
  