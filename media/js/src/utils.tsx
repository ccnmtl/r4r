import { ReactNode } from 'react';

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
    username: string | undefined
    email: string | undefined
}


export interface TeamProps {
    course_id: number
    members: UserProps[]
}


export const authUser = window.r4r.currentUser;
