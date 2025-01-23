-- Creazione del database scuola
CREATE DATABASE scuola;

-- Utilizzo del database scuola
USE scuola;

-- Creazione della tabella studenti
CREATE TABLE studenti (  
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        cognome VARCHAR(50) NOT NULL,
        data_nascita DATE NOT NULL,
        classe VARCHAR(10) NOT NULL,
        email VARCHAR(100) NOT NULL    
);

-- Creazione della tabella docenti
CREATE TABLE docenti (
    
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        cognome VARCHAR(50) NOT NULL,
        materia VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL

);

-- Creazione della tabella lezioni
CREATE TABLE lezioni (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_studente INT NOT NULL,
    id_docente INT NOT NULL,
    data_lezione DATE NOT NULL,
    ora_inizio TIME NOT NULL,
    ora_fine TIME NOT NULL,
    FOREIGN KEY (id_studente) REFERENCES studenti(id),
    FOREIGN KEY (id_docente) REFERENCES docenti(id)
);


-- Query per ottenere tutti gli studenti che hanno lezioni con il docente "Rossi"
SELECT studenti.nome, studenti.cognome
FROM studenti
JOIN lezioni ON studenti.id = lezioni.id_studente
JOIN docenti ON lezioni.id_docente = docenti.id
WHERE docenti.cognome = 'Rossi';

-- Query per ottenere tutti gli studenti che hanno lezioni il 2021-05-10
SELECT studenti.nome, studenti.cognome
FROM studenti
JOIN lezioni ON studenti.id = lezioni.id_studente
WHERE lezioni.data_lezione = '2021-05-10';

