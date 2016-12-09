// @flow

import { combineReducers } from 'redux'
import configureStore from './CreateStore'
import rootSaga from '../Sagas/'
import gameReducer from '../Containers/HomeScreen/reducers';

export default () => {
  /* ------------- Assemble The Reducers ------------- */
  const rootReducer = combineReducers({
    temperature: require('./TemperatureRedux').reducer,
    game: gameReducer
  })

  return configureStore(rootReducer, rootSaga)
}
