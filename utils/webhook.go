package utils

import (
	"context"
	"errors"
	"os"
)

func SetupWebhook(tg *TelegramClient) error {
	webhookURL := os.Getenv("WEBHOOK_URL")
	secret := os.Getenv("WEBHOOK_SECRET")

	if webhookURL == "" {
		return errors.New("WEBHOOK_URL not set")
	}

	if secret == "" {
		return errors.New("WEBHOOK_SECRET not set")
	}

	payload := map[string]any{
		"url":          webhookURL,
		"secret_token": secret,
	}

	_, err := tg.Call(context.Background(), "setWebhook", payload)
	return err
}
