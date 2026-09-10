import 'dart:math';
import 'dart:io';

class Minesweeper {
  final int rows;
  final int cols;
  final int mines;
  List<List<String>> grid;
  List<List<bool>> revealed;

  Minesweeper(this.rows, this.cols, this.mines)
      : grid = List.generate(rows, (_) => List.filled(cols, '0')),
        revealed = List.generate(rows, (_) => List.filled(cols, false)) {
    _placeMines();
    _calculateNumbers();
  }

  void _placeMines() {
    var random = Random();
    int placedMines = 0;

    while (placedMines < mines) {
      int row = random.nextInt(rows);
      int col = random.nextInt(cols);

      if (grid[row][col] != 'M') {
        grid[row][col] = 'M';
        placedMines++;
      }
    }
  }

  void _calculateNumbers() {
    for (int row = 0; row < rows; row++) {
      for (int col = 0; col < cols; col++) {
        if (grid[row][col] == 'M') continue;

        int mineCount = 0;
        for (int i = -1; i <= 1; i++) {
          for (int j = -1; j <= 1; j++) {
            int newRow = row + i;
            int newCol = col + j;
            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] == 'M') {
              mineCount++;
            }
          }
        }
        grid[row][col] = mineCount.toString();
      }
    }
  }

  void revealCell(int row, int col) {
    if (row < 0 || row >= rows || col < 0 || col >= cols || revealed[row][col]) return;

    revealed[row][col] = true;
    if (grid[row][col] == '0') {
      for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
          revealCell(row + i, col + j);
        }
      }
    }
  }

  void printGrid() {
    for (int row = 0; row < rows; row++) {
      for (int col = 0; col < cols; col++) {
        if (revealed[row][col]) {
          stdout.write(grid[row][col] + ' ');
        } else {
          stdout.write('* ');
        }
      }
      print('');
    }
  }
}

void main() {
  Minesweeper game = Minesweeper(5, 5, 5);
  game.printGrid();

  while (true) {
    print('Enter row and column to reveal (e.g., 1 1): ');
    int row = int.parse(stdin.readLineSync()!);
    int col = int.parse(stdin.readLineSync()!);

    game.revealCell(row, col);
    game.printGrid();
  }
}