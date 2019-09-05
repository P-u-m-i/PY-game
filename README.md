# comandi git:
  per aggiungere file all'index:
  
    GIT ADD --ALL
  
  per committare i file:
  
    GIT COMMIT -AM "messaggio"
  
  per pushare:
  
    GIT PUSH ORIGIN MASTER
  
  per pullare:
    
    GIT PULL ORIGIN MASTER
  
  ## ricorda di mettere sempre il file .gitignore prima di pushare!
  se hai problemi consulta https://rogerdudler.github.io/git-guide/
  
# comandi mysql:
  per accedere al terminale MYSQL apri il terminale normale e digita:
  
    MYSQL -U "nome-utente" -p   
  successivamete dovrai inserira la password corrispodente all'utente selezionato;

  una volta dentro con il comando:
  
    SHOW DATABASES; 
  potrai vedere i databases disponibili

  per selezionarne uno usa: 
  
    "USE nome-db"

  una volta selezionato potrai eseguire tutte le query che vuoi:
  ad esempio se vuoi vedere i dati inseriti scrivi;
  
    SELECT * FROM nome-db;
    
# comandi node:

  entra nella cartella db da terminale e digita:
  
      node . create-tables.sql
  o
  
    node . delete-tables.sql
