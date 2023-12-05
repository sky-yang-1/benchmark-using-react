/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 */
import type {Request} from 'react-server/src/ReactFizzServer';

export * from 'react-dom-bindings/src/server/ReactFizzConfigDOM';

export const supportsRequestStorage = false;
export const requestStorage: AsyncLocalStorage<Request> = (null: any);
