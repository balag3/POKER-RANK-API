from flask import Flask, render_template, jsonify, redirect, url_for, request
from card import Card
from evaluator import Evaluator

app = Flask('PokerHandEvaluator')


def card_parser(arg):
    return [Card.new(arg[i:i+2]) for i in range(0, len(arg), 2) if i+1 <= len(arg)]


@app.route('/<hand>/<board>', methods=['GET'])
def main(hand, board):
    try:
        board = card_parser(board)
        hand = card_parser(hand)
        evaluator = Evaluator()
        strength = evaluator.evaluate(board, hand)
        rank = evaluator.class_to_string(evaluator.get_rank_class(strength))
        return jsonify(
            dict(
                rank=rank,
                strength=strength
            )
        )
    except (IndexError, KeyError):
        return "Check your syntax!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1111')
