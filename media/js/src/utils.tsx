import { ReactNode } from 'react';

export interface CourseProps {
    code: string
    details: string | ReactNode
    id: number
    title: string
    url: string
    is_active: boolean
    created_at: Date
};


export interface UserProps {
    first_name: string | undefined
    is_staff: boolean
    is_superuser: boolean
    last_name: string | undefined
    id: number
    username: string | undefined
    email: string | undefined
}


export interface TeamProps {
    course_id: number
    members: UserProps[]
}


export const authUser = window.r4r.currentUser;
