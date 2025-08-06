CREATE TABLE produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    prix DECIMAL(10,2),
    description TEXT
);

INSERT INTO produits (nom, prix, description) VALUES
('Chaussures', 49.99, 'Chaussures confortables pour tous les jours.'),
('T-shirt', 19.99, 'T-shirt 100% coton.'),
('Casque Bluetooth', 79.99, 'Casque sans fil avec réduction de bruit.'),
('Sac à dos', 39.99, 'Sac à dos robuste et imperméable.'),
('Montre connectée', 129.99, 'Montre intelligente avec cardiofrequencemetre.');
