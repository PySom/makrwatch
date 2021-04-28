import { useState } from 'react';

export const useInput = (val, type) => {
    const [value, setValue] = useState(val);
    const onChange = (e) => {
        const { target: { value } } = e;
        setValue(value);
    }
    return {
        type: type || 'text', value, onChange,
    }
}
