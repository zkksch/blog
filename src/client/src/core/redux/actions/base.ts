import { action } from 'typesafe-actions';
import { Action, ActionCreator, Dispatch, AnyAction } from 'redux';
import { ThunkAction, ThunkDispatch } from 'redux-thunk';

export function createAsyncAction<S> (
    before: (state: S) => Action,
    result: (result: any, state: S) => Action,
    error: (error: Error, state: S) => Action,
    coroutine: (state: S, ...args: any[]) => Promise<any>,
    args: any[],
): ActionCreator<
    ThunkAction<
        Promise<Action>,
        S,
        {},
        AnyAction
    >
> { 
    return () => {
        return async (dispatch: ThunkDispatch<S, void, AnyAction>, getState: () => S): Promise<Action> => {
            try {
                dispatch(before(getState()));
                let resultData = await coroutine(getState(), ...args);
                return dispatch(result(resultData, getState()));
            } catch (e) {
                return dispatch(error(e, getState()));
            }
        };
    }
}
