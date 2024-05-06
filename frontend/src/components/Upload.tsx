import { Button } from '@mui/material';

export const Upload = () => {
    const handleUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files && event.target.files[0];
        if (file) {
            // handle file upload
            console.log(file);
        }
    };

    return (
        <div className="p-4">
            <input
                type="file"
                accept="image/*"
                onChange={handleUpload}
                className="hidden"
                id="upload-input"
            />
            <label htmlFor="upload-input">
                <Button variant="contained" component="span">
                    Upload Image
                </Button>
            </label>
        </div>
    );
};
