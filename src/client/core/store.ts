import { createStore, compose, applyMiddleware, Middleware } from 'redux';
import _rootReducer from './reducers';


function configureStore(initialState?: {}) {
    const middlewares: Middleware[] = [];
    const enhancer = compose(applyMiddleware(...middlewares));
    const store = createStore(_rootReducer, initialState!, enhancer);
    return store;
}

var _store = configureStore();

export default _store;
