Use LDDProject



IF EXISTS (SELECT * FROM sys.triggers WHERE object_id = OBJECT_ID(N'[dbo].[trg_AfterDeleteOnFichier]'))
    DROP TRIGGER [dbo].[trg_AfterDeleteOnFichier];
GO

CREATE TRIGGER trg_AfterDeleteOnFichier
ON Fichier
AFTER DELETE
AS
BEGIN
    DELETE FROM MembreVisualiseFichier WHERE Fichier_ID IN (SELECT Fichier_ID FROM deleted)
    DELETE FROM MembreRechercheFichier WHERE Fichier_ID IN (SELECT Fichier_ID FROM deleted)
    DELETE FROM InternauteRechercheFichier WHERE Fichier_ID IN (SELECT Fichier_ID FROM deleted)
    DELETE FROM MotsIndexFichier WHERE Fichier_ID IN (SELECT Fichier_ID FROM deleted)
END

GO
-- Procédure pour mettre à jour le profil d'un membre
CREATE PROCEDURE UpdateMemberProfile
    @Membre_ID INT,
    @NouveauPseudo VARCHAR(255),
    @NouveauEmail VARCHAR(255),
    @NouveauMotdePasse VARCHAR(255),
    @NouvelleImageProfil VARCHAR(255)
AS
BEGIN
    UPDATE Membre
    SET Pseudo = @NouveauPseudo,
        Email = @NouveauEmail,
        MotdePasse = @NouveauMotdePasse,
        ImageProfil = @NouvelleImageProfil
    WHERE Membre_ID = @Membre_ID;
END;
GO


ALTER TABLE Membre
ADD DerniereConnexion DATETIME;
GO
CREATE PROCEDURE MemberLogin
    @Email VARCHAR(255),
    @MotdePasse VARCHAR(255)
AS
BEGIN
    -- Vérifier si les informations d'identification sont valides
    IF EXISTS (SELECT 1 FROM Membre WHERE Email = @Email AND MotdePasse = @MotdePasse)
    BEGIN
        -- Mettre à jour les informations de connexion du membre
        UPDATE Membre SET DerniereConnexion = GETDATE() WHERE Email = @Email;

        -- Retourner un statut de succès ou un message d'accueil, selon vos besoins
        SELECT 'Connexion réussie' AS Status;
    END
    ELSE
    BEGIN
        -- Retourner un statut d'échec ou un message d'erreur, selon vos besoins
        SELECT 'Identifiants incorrects. Veuillez réessayer.' AS Status;
    END
END;
GO

