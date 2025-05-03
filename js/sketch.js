class Knight {
    getMoveOffsets() {
        return [
            [2, 1], [2, -1], [-2, 1], [-2, -1],
            [1, 2], [1, -2], [-1, 2], [-1, -2]
        ];
    }
}

class ChessBoard {
    constructor(knight) {
        this.knight = knight;
        this.board = Array.from({ length: 8 }, () => Array(8).fill(0));
    }

    isWithinBounds(row, col) {
        return row >= 0 && row < 8 && col >= 0 && col < 8;
    }

    isVisited(row, col) {
        return this.board[row][col] > 0;
    }

    markVisited(row, col, step) {
        this.board[row][col] = step;
    }

    unmarkVisited(row, col) {
        this.board[row][col] = 0;
    }

    getPossibleMoves(row, col) {
        const offsets = this.knight.getMoveOffsets();
        const moves = [];
        for (const [dr, dc] of offsets) {
            const newRow = row + dr;
            const newCol = col + dc;
            if (this.isWithinBounds(newRow, newCol) && !this.isVisited(newRow, newCol)) {
                moves.push([newRow, newCol]);
            }
        }
        return moves;
    }
}

function findTour(board, position, step, path) {
    if (step === 64) {
        return true;
    }
    const [row, col] = position;
    const moves = board.getPossibleMoves(row, col);
    for (const move of moves) {
        const [newRow, newCol] = move;
        board.markVisited(newRow, newCol, step + 1);
        path.push(move);
        if (findTour(board, move, step + 1, path)) {
            return true;
        }
        board.unmarkVisited(newRow, newCol);
        path.pop();
    }
    return false;
}

function bruteForceKnightTour(startPosition) {
    const knight = new Knight();
    const board = new ChessBoard(knight);
    const [startRow, startCol] = startPosition;
    board.markVisited(startRow, startCol, 1);
    const path = [startPosition];
    if (findTour(board, startPosition, 1, path)) {
        return path;
    }
    return [];
}

let tourSequence = [];
let currentStep = 0;
let nextMoveTime = 0;
const delay = 500; // milliseconds

function setup() {
    createCanvas(400, 400);
    textSize(16);
    textAlign(CENTER, CENTER);
    const startPosition = [0, 0];
    tourSequence = bruteForceKnightTour(startPosition);
    if (tourSequence.length > 0) {
        console.log(`Tour found with ${tourSequence.length} steps.`);
        nextMoveTime = millis() + delay;
    } else {
        console.log("No tour found.");
    }
}

function draw() {
    background(255);
    drawBoard();
    if (tourSequence.length > 0 && currentStep < tourSequence.length) {
        for (let i = 0; i <= currentStep; i++) {
            const [row, col] = tourSequence[i];
            drawStepNumber(row, col, i + 1);
        }
        const [row, col] = tourSequence[currentStep];
        drawKnight(row, col);
        if (millis() > nextMoveTime) {
            currentStep++;
            if (currentStep < tourSequence.length) {
                nextMoveTime = millis() + delay;
            }
        }
    }
}

function drawBoard() {
    const squareSize = 50;
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            fill((i + j) % 2 === 0 ? 255 : 100);
            rect(j * squareSize, i * squareSize, squareSize, squareSize);
        }
    }
}

function drawKnight(row, col) {
    const squareSize = 50;
    const x = col * squareSize + squareSize / 2;
    const y = row * squareSize + squareSize / 2;
    fill(255, 0, 0);
    ellipse(x, y, 20, 20);
}

function drawStepNumber(row, col, step) {
    const squareSize = 50;
    const x = col * squareSize + squareSize / 2;
    const y = row * squareSize + squareSize / 2;
    fill(0);
    text(step, x, y);
}