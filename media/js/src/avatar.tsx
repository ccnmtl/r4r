import React from 'react';
import { authUser, initials } from './utils';

interface AvatarProps {
    text: string | undefined
    size: string | undefined
    className: string
}

// Initials in a tinted circle. `size` maps to an .avatar-* class.
export default function Avatar({text, size,
    className = 'bg-primary-subtle text-primary-emphasis' }:AvatarProps
) {
    const sizeCls = size ? 'avatar-' + size : 'avatar';

    return <span className={`
        rounded-circle ${className} d-inline-flex align-items-center 
        justify-content-center fw-bold flex-shrink-0 ${sizeCls}`}
    >
        {text ?? initials(authUser)}
    </span>;
}
