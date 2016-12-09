
import * as types from './constants'

export const startGameRequest = () => ({
  type: types.START_GAME_REQUESTED
})

export const goalScored = (player) => ({
  type: types.GOAL_SCORED,
  player
})

export const stopGame = () => {
  return ({
    type: types.STOP_GAME_REQUESTED
  })
}
