import { AppBar, Toolbar, Typography } from '@mui/material';

export const Header = () => (
    <AppBar position="static">
        <Toolbar>
            <Typography variant="h6" component="div">
                Surf Insights
            </Typography>
        </Toolbar>
    </AppBar>
);
