import axios from 'axios';
import { ReactNode } from 'react';
import { COURSEWORKS_API } from './local';


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
};


export interface TeamProps {
    course_id: number
    members: UserProps[]
};


export const authUser = window.r4r.currentUser;


export const importRoster = async(courseId:number) => {
    return await axios.get(
        `https://courseworks2.columbia.edu/api/v1/course/${courseId}/users
        ?per_page=1000`,{headers: {
            Authorization: `Bearer ${COURSEWORKS_API}`}});
};