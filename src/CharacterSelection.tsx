import React from 'react';

interface Character {
    name: string;
    image: string;
    mode: string;
}

const characters: Character[] = [
    { name: 'MCQ', image: '/images/qcm.png', mode: 'qcm' },
    { name: 'Fill in the blanks', image: '/images/texte à trous.png', mode: 'textes_a_trous' },
    { name: 'Find the word', image: '/images/correspondances.png', mode: 'jeux_de_correspondance' }
];

const CharacterSelection: React.FC = () => {
    const handleCharacterClick = (mode: string) => {
        // Redirection vers le mode sélectionné
        console.log(`Selected mode: ${mode}`);
    };

    return (
        <div className="character-selection">
            <h1>Select a character and a game mode</h1>
            <div className="characters">
                {characters.map((character) => (
                    <div
                    key={character.name}
                    className="character-card"
                    onClick={() => handleCharacterClick(character.mode)}
                    >
                        <img src={character.image} alt={character.name} />
                        <h2>{character.name}</h2>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default CharacterSelection;