Use LDDProject


--Requêtes simples
SELECT * FROM Membre;
SELECT * FROM Fichier WHERE Type = 'jpg';
SELECT Nom, Prenom, Email FROM Administrateur;
SELECT Nom, Description FROM Theme;
SELECT * FROM MOTCLE;

--Sélection des membres qui ont visualiser le fichier 2
SELECT M.Pseudo, M.Email
FROM Membre M
JOIN MembreVisualiseFichier MVF ON M.Membre_ID = MVF.Membre_ID
WHERE MVF.Fichier_ID = 2;

-- Sélection des fichiers qui ont été téléchargés par des membres agés de moins de 20 ans
SELECT F.*
FROM Fichier F
JOIN Membre M ON F.MembreID = M.Membre_ID
WHERE DATEDIFF(YEAR, M.DateNaissance, GETDATE()) < 40;

--Sélections des fichiers qui ont le mot clé Écologie
SELECT F.*
FROM Fichier F
JOIN MotsIndexFichier MIF ON F.Fichier_ID = MIF.Fichier_ID
JOIN MOTCLE MC ON MIF.MotCleID = MC.MotCleID
WHERE MC.MotCle = 'Écologie';

--Sélections des membres qui ont recherché un fichier mais qui ne l'ont regardé
SELECT M.*
FROM Membre M
JOIN MembreRechercheFichier MRF ON M.Membre_ID = MRF.Membre_ID
LEFT JOIN MembreVisualiseFichier MVF ON M.Membre_ID = MVF.Membre_ID
WHERE MVF.Membre_ID IS NOT NULL;

--Sélection des thèmes avec le nombre total de fichiers associés à chaque thème (trie par ordre décroissant du nombre de fichiers) :
SELECT 
    T.Nom AS Nom_Theme,
    COUNT(F.ThemeID) AS Nombre_Fichiers_Associés
FROM 
    Theme T
LEFT JOIN 
    Fichier F ON T.ThemeID = F.ThemeID
GROUP BY 
    T.Nom
ORDER BY 
    Nombre_Fichiers_Associés DESC;