
CREATE TABLE Estudiante (
  id INT PRIMARY KEY AUTO_INCREMENT,
  numero_lista INT,
  genero VARCHAR(255),
  grupo VARCHAR(255)
);

CREATE TABLE Maestro (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre_usuario VARCHAR(255),
  contrasena VARCHAR(255)
);

CREATE TABLE Puntuacion (
  id INT PRIMARY KEY AUTO_INCREMENT,
  valor INT,
  nivel INT,
  id_estudiante INT,
  fecha DATETIME,
  FOREIGN KEY (id_estudiante) REFERENCES Estudiante(id)
);

CREATE TABLE Admin (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre_usuario VARCHAR(255),
  contrasena VARCHAR(255)
);