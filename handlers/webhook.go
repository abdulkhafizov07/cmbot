package handlers

import (
	"abdulkhafizov07/cmbot/utils"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

type WebhookHandler struct {
	tg *utils.TelegramClient
}

func NewWebhookHandler(tg *utils.TelegramClient) *WebhookHandler {
	return &WebhookHandler{tg: tg}
}

func (h *WebhookHandler) Handle(c *gin.Context) {
	expected := os.Getenv("WEBHOOK_SECRET")
	received := c.GetHeader("X-Telegram-Bot-Api-Secret-Token")

	if expected == "" || received != expected {
		c.AbortWithStatus(http.StatusUnauthorized)
		return
	}

	var update utils.Update

	if err := c.ShouldBindJSON(&update); err != nil {
		c.AbortWithStatus(http.StatusBadRequest)
		return
	}

	if update.Message.Text == "" {
		c.Status(200)
		return
	}

	text := update.Message.Text
	chatID := update.Message.Chat.ID

	switch text {
	case "/start":
		h.tg.Reply(chatID, "Welcome 👋")

	default:
		h.tg.Reply(chatID, "You said: "+text)
	}

	c.JSON(200, gin.H{"status": "ok"})
}
