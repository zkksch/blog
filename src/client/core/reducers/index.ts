import { combineReducers } from 'redux';
import { ActionType, StateType } from 'typesafe-actions';

import * as actions from '../actions';
import * as actionType from '../actions/constants';
import { Post } from '../models/post';

export type State = {
    readonly post: {
        posts: Post[],
    },
}

export type Action = ActionType<typeof actions>;

const rootReducer = combineReducers<State, Action>({
    post (state = { posts: [] }, action) {
        switch (action.type) {
            case actionType.LOAD_POSTS:
                return {
                    posts: action.payload
                };
            default:
                return state;
        }
    }
});

export type RootState = StateType<typeof rootReducer>;

export default rootReducer;
