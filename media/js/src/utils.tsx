import React, { ReactNode } from 'react';
import { Route } from 'react-router-dom';

export interface TaskProps {
    details: string
}

interface DayProps {
    details: string
    tasks: TaskProps[]
    title: string
}

export interface CaseProps {
    title:string
    days: DayProps[]
}

export interface RotationProps {
    title: string
    cases: CaseProps[]
}

export interface CourseProps {
    code: string
    created_at: Date
    details: string | ReactNode
    id: number
    is_active: boolean
    rotations: RotationProps[]
    title: string
    url: string
}

export interface UserProps {
    first_name: string | undefined
    is_staff: boolean
    is_superuser: boolean
    last_name: string | undefined
    id: number
    username: string
    email: string | undefined
}

export interface TeamProps {
    course_id: number
    members: UserProps[]
}

export interface RouteItem {
    path: string
    el: React.JSX.Element
}

export function toTitleCase(text: string) {
    return text
        .replace(/\w+/g, val => val.charAt(0).toUpperCase() + val.substring(1))
        .replace('-', ' ');
}

export function generateNestedRoute(parent:RouteItem, children:RouteItem[]) {
    return <Route path={parent.path} element={parent.el}>
        <Route index element={children[0].el} />
        {children.map(({path, el}, i) =>
            <Route key={i} path={path} element={el} />)}
    </Route>;
}

export const authUser = window.r4r.currentUser;


export const initials = (user:UserProps) => {
    if (user.first_name && user.last_name) {
        return user.first_name[0] + user.last_name[0];
    } else if (user.first_name) {
        return user.first_name.slice(0, 2);
    } else if (user.last_name) {
        return user.last_name.slice(0, 2);
    } else {
        return user.username.slice(0, 2);
    }
};

export const months = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];