import { action } from 'typesafe-actions';

import * as actionType from './constants';
import { Post } from '../models/post';

export const loadPosts = (...posts: Post[]) => action(actionType.LOAD_POSTS, posts);
