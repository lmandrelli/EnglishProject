import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
    },
    email: {
        type: String,
        required: true,
        unique: true,
    },
    password: {
        type: String,
        required: true,
    },
    progress: {
        type: Map,
        of: Number,
        default: {},
    },
});

const User = mongoose.model('User', UserSchema);
export default User;