import { Drawer, List, ListItem, ListItemText, Divider } from '@mui/material';
import { Upload } from './Upload';

const drawerWidth = 240;

export const SideBar = () => (
    <Drawer
        variant="permanent"
        sx={{ width: drawerWidth, flexShrink: 0 }}
        PaperProps={{ style: { width: drawerWidth } }}
    >
        <List>
            <ListItem>
                <ListItemText primary="Upload" />
            </ListItem>
            <Divider />
            <Upload />
        </List>
    </Drawer>
);
