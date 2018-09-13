import { combineReducers } from 'redux';
import { ActionType, StateType } from 'typesafe-actions';

import * as actions from 'core/redux/actions';
import * as actionType from 'core/redux/actions/constants';

export type State = {
    posts: string[]
}

export type Action = ActionType<typeof actions>;

const rootReducer = combineReducers<State, Action>({
    posts (state = [], action) {
        switch (action.type) {
            case actionType.SET_POST_REQUEST:
                return ['LOADING ...'];
            case actionType.SET_POST_SUCCESS:
                return action.payload;
            case actionType.SET_POST_FAILURE:
                return ['ERROR'];
            default:
                return state;
        }
    }
});

export type RootState = StateType<typeof rootReducer>;

export default rootReducer;
