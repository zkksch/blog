import { createStore, compose, applyMiddleware, Middleware } from 'redux';
import thunk from 'redux-thunk';

import _rootReducer from 'core/redux/reducers';


function configureStore(initialState?: {}) {
    const middlewares: Middleware[] = [
        thunk,
    ];
    const enhancer = compose(applyMiddleware(...middlewares));
    const store = createStore(_rootReducer, initialState!, enhancer);
    return store;
}

var _store = configureStore();

export default _store;
