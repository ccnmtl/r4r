import React from 'react';

export default function BrandMark({ size = 'md', solid = false }) {
    const cls = [
        'brand-mark', 'rounded-2', 'd-inline-flex', 'align-items-center',
        'justify-content-center', 'fw-bold'
    ];

    if (size === 'sm') cls.push('brand-mark--sm');
    if (solid) cls.push('brand-mark--solid');

    return <span className={cls.join(' ')}>R4R</span>;
}
