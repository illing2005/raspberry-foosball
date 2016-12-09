
import {START_GAME_REQUESTED, GOAL_SCORED, STOP_GAME_REQUESTED} from './constants'

const initialState = {
  score: [0, 0]
}

const checkGameStatus = (score) => {
  if (score[0] >= 10 || score[1]  >= 10) {
    if (Math.abs(score[0] - score[1]) < 2)
      return 'overtime';
    return 'over';
  }
  return 'running'
}

const gameReducer = (state=initialState, action) => {

  switch (action.type) {
    case START_GAME_REQUESTED:
      return {...state, status: 'running', score: [0, 0]};
    case GOAL_SCORED:
      const newScore = [...state.score];
      newScore[action.player] += 1;
      return {...state, score: newScore, status: checkGameStatus(newScore)};
    case STOP_GAME_REQUESTED:
      return initialState
    default:
      return state;
  }
};


export default gameReducer;
