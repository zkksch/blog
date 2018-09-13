import { action } from 'typesafe-actions';
import { Action, ActionCreator, Dispatch, AnyAction } from 'redux';
import { ThunkAction, ThunkDispatch } from 'redux-thunk';

import * as actionType from 'core/redux/actions/constants';
import { State } from 'core/redux/reducers';

export const loadingPosts = () => action(actionType.SET_POST_REQUEST);
export const setPosts = (...posts: string[]) => action(actionType.SET_POST_SUCCESS, posts);
export const setPostsErr = () => action(actionType.SET_POST_FAILURE);

export const requestPosts: ActionCreator<
    ThunkAction<
        Promise<Action>,
        State,
        {},
        AnyAction
    >
> = () => {
    return async (dispatch: ThunkDispatch<State, void, AnyAction>, getState: () => State): Promise<Action> => {
        try {
            dispatch(loadingPosts());
            let response = await fetch('/post/');
            let data = await response.json();
            return dispatch(setPosts(...data.map( (el: {title: string}) => el.title )));
        } catch (e) {
            return dispatch(setPostsErr());
        }
    };
};
